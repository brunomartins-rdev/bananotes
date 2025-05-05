takeANote = function(btnId, formId) {
  const btn = document.getElementById(btnId)

  const form = document.getElementById(formId)

  if (btn && form) {
    btn.style.display = 'none';
    form.style.display = 'block';
  }
}
