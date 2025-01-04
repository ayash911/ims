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

            const grade = document.createElement("span");
            grade.style.fontWeight = "bold";
            grade.style.color = "#333";
            grade.innerText = ", Grade: ";

            const gradeValue = document.createElement("span");
            gradeValue.style.fontStyle = "italic";
            gradeValue.style.color = "#007BFF";
            gradeValue.innerText = `${Product.grade}`;

            const thickness = document.createElement("span");
            thickness.style.fontWeight = "bold";
            thickness.style.color = "#333";
            thickness.innerText = ", Thickness: ";

            const thicknessValue = document.createElement("span");
            thicknessValue.style.fontStyle = "italic";
            thicknessValue.style.color = "#007BFF";
            thicknessValue.innerText = `${Product.thickness}`;

            const dimension = document.createElement("span");
            dimension.style.fontWeight = "bold";
            dimension.style.color = "#333";
            dimension.innerText = ", Dimension: ";

            const dimensionValue = document.createElement("span");
            dimensionValue.style.fontStyle = "italic";
            dimensionValue.style.color = "#007BFF";
            dimensionValue.innerText = `${Product.dimension}`;
            

            // Append all elements to the list item
            li.appendChild(id);
            li.appendChild(idValue);
            li.appendChild(name);
            li.appendChild(nameValue);
            li.appendChild(barcode);
            li.appendChild(barcodeValue);
            li.appendChild(grade);
            li.appendChild(gradeValue);
            li.appendChild(thickness);
            li.appendChild(thicknessValue);
            li.appendChild(dimension);
            li.appendChild(dimensionValue);
            

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

// Add product functionality
const addProductForm = document.getElementById("addProductForm");
addProductForm.addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent default form submission
  
  const formData = new FormData(addProductForm);
  const data = {
    grade: formData.get("grade"),
    thickness: formData.get("thickness"),
    dimension: formData.get("dimension")
  };

  console.log(data); // Check the data being sent
  
  fetch("/api/add_product", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    // alert(data.message || "Product added successfully!");
    fetchProducts(); // Refresh the product list after adding a new product
  })
  .catch(error => {
    console.error("Error adding product:", error);
    alert("An error occurred while adding the product. Please try again.");
  });
});

// Update thickness options based on grade
function updateThicknessOptions() {
  const grade = document.getElementById("grade").value;
  const thicknessSelect = document.getElementById("thickness");

  // Clear existing options
  thicknessSelect.innerHTML = "";

  // Populate based on grade
  const options = grade === "B" ? ["05", "08", "11", "16"] : ["05", "09", "12", "18"];
  options.forEach((thickness) => {
    const option = document.createElement("option");
    option.value = thickness;
    option.innerText = thickness;
    thicknessSelect.appendChild(option);
  });
}

// Initialize thickness options on page load
window.onload = updateThicknessOptions;
