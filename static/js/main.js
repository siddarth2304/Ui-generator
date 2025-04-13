document.getElementById("uiForm").addEventListener("submit", async function(e) {
  e.preventDefault();
  const brandColor = document.getElementById("brandColor").value;
  const font = document.getElementById("font").value;
  const layout = document.getElementById("layout").value;
  const headline = document.getElementById("headline").value;

  const response = await fetch("/generate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ brandColor, font, layout, headline })
  });

  const data = await response.json();
  document.getElementById("output").innerHTML = data.html;
});
