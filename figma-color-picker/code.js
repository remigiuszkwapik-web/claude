// Figma Plugin – Persistent Color Picker
// Öffnet die UI und hält sie dauerhaft offen

figma.showUI(__html__, {
  width: 300,
  height: 420,
  title: "Color Picker",
  themeColors: true,
});

// Plugin bleibt offen bis der Nutzer es manuell schließt
// Nachrichten von der UI empfangen (für spätere Erweiterungen)
figma.ui.onmessage = (msg) => {
  if (msg.type === "close") {
    figma.closePlugin();
  }
};
