document.getElementById("checkInventory").addEventListener("click", () => {
    const barcode = document.getElementById("barcodeInput").value.trim();
  
    fetch(`/api/inventory${barcode ? `?barcode=${encodeURIComponent(barcode)}` : ""}`) // Add query param only if barcode is present
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        const inventoryInfo = document.getElementById("inventoryInfo");
        inventoryInfo.innerHTML = ""; // Clear previous content
  
        if (data.success) {
          if (data.inventory.length === 0) {
            inventoryInfo.innerText = "No inventory found.";
          } else {
            // Display inventory data
            data.inventory.forEach((item) => {
              const itemDiv = document.createElement("div");
              itemDiv.innerText = `ID: ${item.id}, Product ID: ${item.product_id}, Location: ${item.location}, Quantity: ${item.quantity}`;
              inventoryInfo.appendChild(itemDiv);
            });
          }
        } else {
          inventoryInfo.innerText = data.message || "Item not found in inventory.";
        }
      })
      .catch((error) => {
        console.error("Error fetching inventory:", error);
        alert("An error occurred while fetching inventory. Please try again.");
      });
  });
  
  