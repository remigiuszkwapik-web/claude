// Figma Plugin – Persistent Color Picker
figma.showUI(__html__, {
  width: 240,
  height: 520,
  title: "Color Picker",
  themeColors: true,
});

function readSelectionColor() {
  var sel = figma.currentPage.selection;
  if (sel.length === 0) {
    figma.ui.postMessage({ type: "selection", color: null });
    return;
  }

  var node = sel[0];
  if ("fills" in node && Array.isArray(node.fills) && node.fills.length > 0) {
    var fills = node.fills.slice().reverse();
    var fill = null;
    for (var i = 0; i < fills.length; i++) {
      if (fills[i].type === "SOLID" && fills[i].visible !== false) {
        fill = fills[i];
        break;
      }
    }
    if (fill) {
      figma.ui.postMessage({
        type: "selection",
        color: {
          r: fill.color.r,
          g: fill.color.g,
          b: fill.color.b,
          a: fill.opacity !== undefined ? fill.opacity : 1,
        },
        nodeName: node.name,
      });
      return;
    }
  }

  figma.ui.postMessage({ type: "selection", color: null, nodeName: null });
}

figma.loadAllPagesAsync().then(function () {
  readSelectionColor();

  figma.on("selectionchange", readSelectionColor);

  figma.on("documentchange", function (event) {
    var sel = figma.currentPage.selection;
    var selectionIds = {};
    for (var i = 0; i < sel.length; i++) {
      selectionIds[sel[i].id] = true;
    }
    for (var j = 0; j < event.documentChanges.length; j++) {
      var change = event.documentChanges[j];
      if (
        change.type === "PROPERTY_CHANGE" &&
        selectionIds[change.id] &&
        change.properties.indexOf("fills") !== -1
      ) {
        readSelectionColor();
        return;
      }
    }
  });
});

figma.ui.onmessage = function (msg) {
  if (msg.type === "close") {
    figma.closePlugin();
  }
};
