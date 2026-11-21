"use strict";

const types = {
  domestic: { label: "Nội địa", short: "NĐ", eligible: true, reason: "Giao trễ 26 giờ", rate: 0.5 },
  heavy: { label: "Hàng nặng", short: "HN", eligible: true, reason: "Giao trễ 28 giờ", rate: 0.5 },
  international: { label: "Quốc tế", short: "QT", eligible: false, reason: "Thiếu dữ liệu chặng quốc tế" },
  partner: { label: "Đối tác", short: "ĐT", eligible: false, reason: "Điều khoản hoàn phí riêng" }
};
const states = {
  review: ["Chờ xem lại", "wait"],
  handoff: ["Chuyển CSKH", "neutral"],
  done: ["Đã hoàn", "good"],
  rejected: ["Đã từ chối", "error"]
};
const seeds = [
  [70012, "domestic", 60000, "ok"],
  [70018, "heavy", 520000, "ok"],
  [70023, "international", 185000, "ok"],
  [70031, "domestic", 90000, "error"],
  [70035, "partner", 120000, "ok"]
];

const search = document.querySelector("#search");
const filter = document.querySelector("#filter");
const caseList = document.querySelector("#case-list");
const detail = document.querySelector("#detail");
const dialog = document.querySelector("#create-dialog");
const toast = document.querySelector("#toast");
const money = new Intl.NumberFormat("vi-VN");
let cases;
let selectedId;
let sequence;
let toastTimer;

function log(item, name, message) {
  item.events.push({ name, message });
}

function newCase(number, typeKey, fee, ledgerMode) {
  const type = types[typeKey];
  const item = {
    id: "RF-" + number,
    trace: "demo-" + number,
    type,
    fee,
    ledgerMode,
    status: type.eligible ? "review" : "handoff",
    suggested: type.eligible ? Math.round(fee * type.rate) : null,
    paid: null,
    events: []
  };
  log(item, "refund_request_created", "Tiếp nhận yêu cầu");
  if (type.eligible) {
    log(item, "agent_run_completed", "Tạo gợi ý hoàn " + (type.rate * 100) + "% phí");
  } else {
    log(item, "handoff_to_staff", type.reason);
  }
  return item;
}

function resetDemo() {
  cases = seeds.map(seed => newCase(...seed));
  selectedId = cases[0].id;
  sequence = 70100;
  search.value = "";
  filter.value = "all";
  showView("queue");
  render();
}

function badge(status) {
  const [label, style] = states[status];
  return '<span class="badge ' + style + '">' + label + '</span>';
}

function formatMoney(amount) {
  return amount === null ? "—" : money.format(amount) + " đ";
}

function renderList() {
  const query = search.value.trim().toLocaleLowerCase("vi");
  const results = cases.filter(item => {
    const text = [item.id, item.type.label, item.type.reason].join(" ").toLocaleLowerCase("vi");
    return text.includes(query) && (filter.value === "all" || filter.value === item.status);
  });
  document.querySelector("#case-count").textContent = results.length + " yêu cầu";
  caseList.innerHTML = results.length ? results.map(item => {
    const selected = item.id === selectedId;
    return '<button type="button" class="case' + (selected ? ' selected' : '') +
      '" data-id="' + item.id + '" aria-pressed="' + selected + '"><span class="case-avatar" aria-hidden="true">' +
      item.type.short + '</span><span class="case-desc"><strong>' + item.id + ' · ' +
      item.type.label + '</strong><span>' + item.type.reason + '</span></span>' + badge(item.status) + '</button>';
  }).join("") : '<p class="empty">Không tìm thấy yêu cầu.</p>';
}

function caseActions(item) {
  if (item.status === "done") {
    return '<button class="button" data-action="retry">Thử gửi lại yêu cầu</button>';
  }
  if (item.status !== "review") return "";
  return '<button class="button primary" data-action="approve">Duyệt hoàn phí</button>' +
    '<button class="button" data-action="edit" aria-controls="edit-form" aria-expanded="false">Sửa số tiền</button>' +
    '<button class="button" data-action="handoff">Chuyển CSKH</button>' +
    '<button class="button danger" data-action="reject">Từ chối</button>';
}

function renderDetail() {
  const item = cases.find(entry => entry.id === selectedId);
  if (!item) return;
  const scope = item.type.eligible
    ? '<strong>Trong phạm vi</strong><span>Loại yêu cầu đủ điều kiện pilot.</span>'
    : '<strong>Ngoài phạm vi</strong><span>' + item.type.reason + '. Nhân viên CSKH tiếp nhận.</span>';
  const events = item.events.map(event => '<li><div><code>' + event.name + '</code><br>' + event.message + '</div></li>').join("");
  const ledgerLabel = item.status === "done" ? "Số tiền đã hoàn" : "Gợi ý hoàn phí";
  const amount = item.status === "done" ? item.paid : item.suggested;
  detail.innerHTML = '<div class="detail-head"><div class="panel-title"><h2>' +
    item.id + ' · ' + item.type.label + '</h2>' + badge(item.status) +
    '</div><p>' + item.type.reason + ' · Trace ' + item.trace + '</p></div>' +
    '<div class="detail-body"><div class="guard ' + (item.type.eligible ? '' : 'blocked') + '">' + scope + '</div>' +
    '<div class="money"><div><span>Phí vận chuyển</span><strong>' + formatMoney(item.fee) +
    '</strong></div><div><span>' + ledgerLabel + '</span><strong class="offer">' + formatMoney(amount) + '</strong></div></div>' +
    '<div class="actions">' + caseActions(item) + '</div>' +
    '<form class="inline-form" id="edit-form" hidden><label>Số tiền hoàn mới (đ)<input type="number" name="amount" min="1" max="' +
    item.fee + '" value="' + (item.suggested ?? 1) + '" required></label><button class="button primary">Duyệt số tiền mới</button></form>' +
    '<section class="events"><h3>Nhật ký xử lý</h3><ul>' + events + '</ul></section></div>';
}

function render() {
  renderList();
  renderDetail();
}

function notify(message) {
  toast.textContent = message;
  toast.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.hidden = true; }, 3600);
}

function approve(item, amount, edited) {
  if (item.status !== "review" || !item.type.eligible) return;
  log(item, "staff_review_decision", edited ? "Sửa gợi ý thành " + formatMoney(amount) : "Duyệt gợi ý " + formatMoney(amount));
  if (item.ledgerMode === "error") {
    log(item, "refund_ledger_write", "Lỗi 503 khi ghi sổ cái");
    log(item, "handoff_to_staff", "Đối soát giao dịch");
    item.status = "handoff";
    notify("Ghi sổ thất bại. Đã chuyển CSKH để đối soát.");
  } else {
    item.paid = amount;
    item.status = "done";
    log(item, "refund_ledger_write", "Đã ghi " + formatMoney(amount) + " · khóa " + item.trace);
    log(item, "refund_status_notified", "Đã hoàn · mô phỏng");
    notify("Sổ cái đã ghi thành công trong demo.");
  }
  render();
}

function showView(id) {
  document.querySelectorAll(".view").forEach(section => { section.hidden = section.id !== id; });
  document.querySelectorAll(".nav-button").forEach(button => {
    const active = button.dataset.view === id;
    button.classList.toggle("active", active);
    if (active) button.setAttribute("aria-current", "page");
    else button.removeAttribute("aria-current");
  });
}

document.querySelector("nav").addEventListener("click", event => {
  const button = event.target.closest("button[data-view]");
  if (button) showView(button.dataset.view);
});
search.addEventListener("input", renderList);
filter.addEventListener("change", renderList);
caseList.addEventListener("click", event => {
  const button = event.target.closest("button[data-id]");
  if (!button) return;
  selectedId = button.dataset.id;
  render();
  caseList.querySelector(".selected")?.focus();
});
detail.addEventListener("click", event => {
  const button = event.target.closest("button[data-action]");
  if (!button) return;
  const item = cases.find(entry => entry.id === selectedId);
  const action = button.dataset.action;
  if (action === "retry" && item.status === "done") {
    log(item, "refund_duplicate_blocked", "Đã có bản ghi sổ cái cho khóa " + item.trace);
    notify("Đã chặn yêu cầu hoàn trùng.");
    render();
    return;
  }
  if (item.status !== "review") return;
  if (action === "approve") {
    approve(item, item.suggested, false);
  } else if (action === "edit") {
    const form = detail.querySelector("#edit-form");
    form.hidden = !form.hidden;
    button.setAttribute("aria-expanded", String(!form.hidden));
    if (!form.hidden) form.elements.amount.focus();
  } else if (action === "handoff" || action === "reject") {
    item.status = action === "handoff" ? "handoff" : "rejected";
    log(item, "staff_review_decision", action === "handoff" ? "Chuyển CSKH" : "Từ chối hoàn");
    if (action === "handoff") log(item, "handoff_to_staff", "Nhân viên sẽ xử lý tiếp");
    notify(states[item.status][0] + ".");
    render();
  }
});
detail.addEventListener("submit", event => {
  if (event.target.id !== "edit-form") return;
  event.preventDefault();
  const item = cases.find(entry => entry.id === selectedId);
  const amount = event.target.elements.amount.valueAsNumber;
  if (Number.isInteger(amount) && amount > 0 && amount <= item.fee) approve(item, amount, true);
});
document.querySelector("#reset").addEventListener("click", () => {
  resetDemo();
  notify("Đã đặt lại dữ liệu mô phỏng.");
});
document.querySelector("#new-case").addEventListener("click", () => dialog.showModal());
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());
document.querySelector("#create-form").addEventListener("submit", event => {
  event.preventDefault();
  const form = event.target;
  const type = form.elements.type.value;
  const fee = form.elements.fee.valueAsNumber;
  const ledger = form.elements.ledger.value;
  if (!Object.hasOwn(types, type) || !Number.isInteger(fee) || fee < 1000 || fee > 100000000) return;
  const item = newCase(sequence++, type, fee, ledger);
  cases.unshift(item);
  selectedId = item.id;
  search.value = "";
  filter.value = "all";
  form.reset();
  dialog.close();
  render();
  notify("Đã tạo yêu cầu " + item.id + ".");
});

resetDemo();
