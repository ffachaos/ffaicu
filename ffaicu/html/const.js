function jump(sel) {
  if (sel.options[sel.selectedIndex].value) {
    location.href = sel.options[sel.selectedIndex].value;
  }
}
function mdown(e) {
  if (navigator.appName == "Microsoft Internet Explorer") {
    if (event.button == 2) {
      alert("�s���s�ׂ͌��ւł��I�I�p������ꍇ�L�������폜���܂��I�I");
      return(false);
    }
  } else if (navigator.appName == "Netscape") {
    if (e.which == 3) {
      alert("�s���s�ׂ͌��ւł��I�I�p������ꍇ�L�������폜���܂��I�I");
      return(false);
    }
  }
}
if (document.all) {
  document.onmousedown = mdown;
}
if (document.layers) {
  window.onmousedown = mdown;
  window.captureEvents(Event.MOUSEDOWN);
}
