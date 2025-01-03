// Check inventory by barcode
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

// Fetch orders and display them
const fetchOrders = () => {
  fetch("/api/orders")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const ordersList = document.getElementById("ordersList");
      ordersList.innerHTML = ""; // Clear the list before populating
      if (data.orders && data.orders.length > 0) {
        data.orders.forEach((order) => {
          const li = document.createElement("li");
          li.innerText = `Order ID: ${order.id}, Status: ${order.status}`;
          ordersList.appendChild(li);
        });
      } else {
        ordersList.innerText = "No orders available.";
      }
    })
    .catch((error) => {
      console.error("Error fetching orders:", error);
      alert("An error occurred while fetching orders. Please try again.");
    });
};

// Call fetchOrders to load orders initially
fetchOrders();
