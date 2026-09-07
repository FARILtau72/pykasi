"use strict";

// All examples are readable HTML. JavaScript only adds selection and copying.
const exampleSelect = document.querySelector("#example-select");
const examples = Array.from(document.querySelectorAll("[data-example]"));
const filename = document.querySelector(".editor-label");
const copyStatus = document.querySelector("#copy-status");
let statusTimeout;

function announce(message) {
  clearTimeout(statusTimeout);
  copyStatus.textContent = message;
  statusTimeout = setTimeout(() => {
    copyStatus.textContent = "";
  }, 5000);
}

function selectExample() {
  const selected = examples.find((example) => example.dataset.example === exampleSelect.value);
  if (!selected) return;
  examples.forEach((example) => {
    example.hidden = example !== selected;
  });
  filename.textContent = selected.dataset.filename;
}

exampleSelect.hidden = false;
exampleSelect.addEventListener("change", selectExample);
// Keep a browser-restored selection consistent with the displayed code.
selectExample();

function selectForManualCopy(element) {
  const selection = window.getSelection();
  if (selection) {
    const range = document.createRange();
    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
  }
  announce("Salin otomatis belum tersedia. Kode sudah dipilih; tekan Ctrl+C atau Cmd+C, atau tahan teks lalu pilih Salin.");
}

async function copyCode(button, element) {
  if (!element) return;
  button.disabled = true;
  try {
    if (!navigator.clipboard || !window.isSecureContext) {
      selectForManualCopy(element);
      return;
    }
    await navigator.clipboard.writeText(element.textContent.trim());
    announce("Tersalin, bre. Tinggal tempel!");
  } catch {
    selectForManualCopy(element);
  } finally {
    button.disabled = false;
  }
}

document.querySelectorAll("[data-copy]").forEach((button) => {
  button.hidden = false;
  button.addEventListener("click", () => {
    copyCode(button, document.getElementById(button.dataset.copy));
  });
});

const copyExample = document.querySelector("[data-copy-example]");
copyExample.hidden = false;
copyExample.addEventListener("click", () => {
  const activeExample = examples.find((example) => !example.hidden);
  copyCode(copyExample, activeExample?.querySelector("[data-source]"));
});
