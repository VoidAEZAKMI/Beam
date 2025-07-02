const sock = new WebSocket(
    (location.protocol === "https:" ? "wss://" : "ws://") +
    location.host + "/ws/notifications/"
);
sock.onmessage = ({data}) => {
    const {message} = JSON.parse(data);
    const box = document.getElementById("ws-alert");
    box.textContent = message;
    box.style.display = "block";
    box.style.opacity = 1;
    setTimeout(() => box.style.opacity = 0, 4000);
};


const $   = q => document.querySelector(q);
const $$  = q => document.querySelectorAll(q);
const csrftoken = "{{ csrf_token }}";

function addRow(id, name, price) {
    const li = document.createElement("li");
    li.id = `product-${id}`;
    li.className = "list-group-item d-flex justify-content-between align-items-center";
    li.innerHTML = `${name} — $${price}
        <div>
          <button class="btn btn-warning btn-sm" onclick="openUpdate(${id}, '${name}', '${price}')">✏️</button>
          <button class="btn btn-danger  btn-sm" onclick="openDelete(${id})">🗑️</button>
        </div>`;
    $("#productList").appendChild(li);
}


$("#createForm").addEventListener("submit", e => {
    e.preventDefault();
    fetch(e.target.action, {method:"POST", body:new FormData(e.target)})
        .then(r=>r.json()).then(d=>{
            if (d.success) addRow(d.product_id, d.product_name, d.product_price);
            e.target.reset();
        });
});


const uModal = new bootstrap.Modal("#updateModal");
$("#updateForm").addEventListener("submit", e=>{
    e.preventDefault();
    fetch(e.target.action, {method:"POST", body:new FormData(e.target)})
        .then(r=>r.json()).then(d=>{
            if (d.success) {
                const row = $(`#product-${d.product_id}`);
                row.firstChild.textContent = `${d.product_name} — $${d.product_price} `;
                uModal.hide();
            }
        });
});
function openUpdate(id, name, price) {
    $("#uName").value  = name;
    $("#uPrice").value = price;
    $("#updateForm").action = `/` + id + `/update/`;  
    uModal.show();
}

const dModal = new bootstrap.Modal("#deleteModal");
$("#deleteForm").addEventListener("submit", e=>{
    e.preventDefault();
    fetch(e.target.action, {method:"POST", headers:{"X-Requested-With":"XMLHttpRequest"}})
        .then(r=>r.json()).then(d=>{
            if (d.success) {
                $(`#product-${d.product_id}`).remove();
                dModal.hide();
            }
        });
});
function openDelete(id){
    $("#deleteForm").action = `/` + id + `/delete/`;
    dModal.show();
}