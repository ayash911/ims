let socket = io.connect('http://localhost:5000');

function scanBarcode(event) {
    const barcode = event.target.value;
    if (barcode.length === 13) {  // Assuming barcode length of 13
        // Send barcode to backend to search product
        fetch(`/api/products/${barcode}`)
            .then(response => response.json())
            .then(data => {
                console.log('Product Found:', data);
            });
    }
}
