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
          li.innerText = `Order ID: ${order.id}, Customer ID: ${order.cust_id}, Product ID: ${order.product_id}, Quantity: ${order.quantity}, Status: ${order.status}`;
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

fetchOrders();
