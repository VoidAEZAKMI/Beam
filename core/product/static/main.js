(function () {
    const scheme     = location.protocol === "https:" ? "wss" : "ws";
    const endpoint   = `${scheme}://${location.host}/ws/notifications/`;
    const log        = document.getElementById("ws-log");
    const MAX_MSG    = 100;                     // сколько сообщений держим в истории
    const LS_KEY     = "ws_history";            // ключ в localStorage

    /* --- 0. Восстановление истории из localStorage --- */
    try {
        const saved = JSON.parse(localStorage.getItem(LS_KEY) || "[]");
        saved.forEach(text => addMsg(text));    // старые в конец (порядок сохранён)
    } catch { /* игнорируем битые данные */ }

    /* --- 1. Подключаемся к WebSocket --- */
    const socket = new WebSocket(endpoint);

    socket.addEventListener("open",   ()   => console.log("WS: connected"));
    socket.addEventListener("error",  err => console.error("WS error:", err));

    /* --- 2. Обработка входящих сообщений --- */
    socket.addEventListener("message", ({data}) => {
        try {
            const {message} = JSON.parse(data);
            addMsg(message, true);              // true = сохранить в localStorage
        } catch(e) {
            console.warn("WS parse fail:", e);
        }
    });

    /* --- вспомогательные функции --- */
    function addMsg(text, save = false) {
        const li = document.createElement("li");
        li.textContent = text;
        log.prepend(li);                        // новое сообщение наверх

        // ограничиваем размер списка в DOM
        while (log.children.length > MAX_MSG) log.lastChild.remove();

        // и в localStorage
        if (save) {
            const history = [...log.querySelectorAll("li")]
                              .slice(0, MAX_MSG)       // берём ровно MAX_MSG
                              .reverse()               // обратно в хронологию
                              .map(li => li.textContent);
            localStorage.setItem(LS_KEY, JSON.stringify(history));
        }
    }
})();