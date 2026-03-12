// Figma Plugin – Persistent Color Picker
figma.showUI(__html__, {
  width: 240,
  height: 520,
  title: "Color Picker",
  themeColors: true,
});

function readSelectionColor() {
  const sel = figma.currentPage.selection;
  if (sel.length === 0) {
    figma.ui.postMessage({ type: "selection", color: null });
    return;
  }

  const node = sel[0];
  if ("fills" in node && Array.isArray(node.fills) && node.fills.length > 0) {
    const fill = [...node.fills].reverse().find(
      (f) => f.type === "SOLID" && f.visible !== false
    );
    if (fill) {
      figma.ui.postMessage({
        type: "selection",
        color: {
          r: fill.color.r,
          g: fill.color.g,
          b: fill.color.b,
          a: fill.opacity ?? 1,
        },
        nodeName: node.name,
      });
      return;
    }
  }

  figma.ui.postMessage({ type: "selection", color: null, nodeName: null });
}

// Selektion beim Start lesen
readSelectionColor();

// Auf Selektionsänderungen reagieren
figma.on("selectionchange", readSelectionColor);

figma.ui.onmessage = (msg) => {
  if (msg.type === "close") {
    figma.closePlugin();
  }
};
