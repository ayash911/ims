// Fetch orders and display them
const fetchProducts = () => {
  fetch("/api/products")
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      const product_list = document.getElementById("product_list");
      product_list.innerHTML = ""; // Clear the list before populating
      if (data.products && data.products.length > 0) {
        data.products.forEach((Product) => {
          function createElement(Product) {
            const li = document.createElement("li");
            // Create attribute and value elements
            const id = document.createElement("span");
            id.style.fontWeight = "bold";
            id.style.color = "#333"; // Darker color for attributes
            id.innerText = "Product ID: ";

            const idValue = document.createElement("span");
            idValue.style.fontStyle = "italic";
            idValue.style.color = "#007BFF"; // Blue for values
            idValue.innerText = `${Product.id}`;

            const name = document.createElement("span");
            name.style.fontWeight = "bold";
            name.style.color = "#333";
            name.innerText = ", Product Name: ";

            const nameValue = document.createElement("span");
            nameValue.style.fontStyle = "italic";
            nameValue.style.color = "#007BFF";
            nameValue.innerText = `${Product.name}`;

            const barcode = document.createElement("span");
            barcode.style.fontWeight = "bold";
            barcode.style.color = "#333";
            barcode.innerText = ", Barcode: ";

            const barcodeValue = document.createElement("span");
            barcodeValue.style.fontStyle = "italic";
            barcodeValue.style.color = "#007BFF";
            barcodeValue.innerText = `${Product.barcode}`;

            // Append all elements to the list item
            li.appendChild(id);
            li.appendChild(idValue);
            li.appendChild(name);
            li.appendChild(nameValue);
            li.appendChild(barcode);
            li.appendChild(barcodeValue);

            product_list.appendChild(li);
          }
          createElement(Product);
        });
      } else {
        product_list.innerText = "No products available.";
      }
    })
    .catch((error) => {
      console.error("Error fetching products:", error);
      alert("An error occurred while fetching products. Please try again.");
    });
};

fetchProducts();
