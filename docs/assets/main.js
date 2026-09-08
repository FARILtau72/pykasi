"use strict";

// Examples stay readable in HTML. JavaScript enhances navigation and copying.
const tabs = Array.from(document.querySelectorAll("[data-example-tab]"));
const panels = Array.from(document.querySelectorAll("[data-example]"));
const tablist = document.querySelector(".example-tabs");
const copyStatus = document.getElementById("copy-status");
const labelTimers = new WeakMap();
let statusTimeout;

function activateTab(tab, moveFocus = false) {
  const selected = panels.find((panel) => panel.dataset.example === tab.dataset.exampleTab);
  if (!selected) return;
  tabs.forEach((item) => {
    const active = item === tab;
    item.setAttribute("aria-selected", String(active));
    item.tabIndex = active ? 0 : -1;
  });
  panels.forEach((panel) => { panel.hidden = panel !== selected; });
  if (moveFocus) tab.focus();
}

if (tablist && tabs.length && panels.length) {
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateTab(tab));
    tab.addEventListener("keydown", (event) => {
      let next;
      if (event.key === "ArrowRight") next = (index + 1) % tabs.length;
      if (event.key === "ArrowLeft") next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === "Home") next = 0;
      if (event.key === "End") next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      activateTab(tabs[next], true);
    });
  });
  activateTab(tabs[0]);
  tablist.hidden = false;
  document.documentElement.classList.add("enhanced");
}

function announce(message) {
  clearTimeout(statusTimeout);
  copyStatus.textContent = message;
  statusTimeout = setTimeout(() => { copyStatus.textContent = ""; }, 6000);
}

function selectForManualCopy(element) {
  const selection = window.getSelection();
  if (selection) {
    const range = document.createRange();
    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
  }
  announce("Salin otomatis belum tersedia. Tekan Ctrl+C atau Cmd+C, atau tahan teks yang dipilih lalu pilih Salin.");
}

async function copyCode(button, element) {
  if (!element || button.getAttribute("aria-busy") === "true") return;
  button.setAttribute("aria-busy", "true");
  try {
    if (!navigator.clipboard || !window.isSecureContext) {
      selectForManualCopy(element);
      return;
    }
    await navigator.clipboard.writeText(element.textContent.trim());
    announce("Tersalin, bre. Tinggal tempel!");
    clearTimeout(labelTimers.get(button));
    button.textContent = "Tersalin ✓";
    labelTimers.set(button, setTimeout(() => { button.textContent = button.dataset.copyLabel; }, 2200));
  } catch {
    selectForManualCopy(element);
  } finally {
    button.removeAttribute("aria-busy");
  }
}

document.querySelectorAll("[data-copy]").forEach((button) => {
  button.dataset.copyLabel = button.textContent.trim();
  button.hidden = false;
  button.addEventListener("click", () => copyCode(button, document.getElementById(button.dataset.copy)));
});
