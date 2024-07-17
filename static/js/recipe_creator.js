document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-ingredient').addEventListener('click', function() {
        const ingredientSelect = document.getElementById('ingredient-select');
        const quantityInput = document.getElementById('ingredient-quantity');

        const ingredientId = ingredientSelect.value;
        const ingredientName = ingredientSelect.options[ingredientSelect.selectedIndex].text;
        const quantity = quantityInput.value;

        if (quantity <= 0) {
            alert('Please enter a valid quantity.');
            return;
        }

        const ingredientList = document.getElementById('ingredient-list');
        const row = document.createElement('tr');

        row.innerHTML = `
            <td>
                <input type="hidden" name="ingredients[]" value="${ingredientId}">
                <input type="hidden" name="quantities[]" value="${quantity}">
                ${ingredientName}
            </td>
            <td>${quantity} Grams</td>
            <td><button type="button" class="btn btn-danger remove-ingredient">Remove</button></td>
        `;

        ingredientList.appendChild(row);

        // Clear the input fields
        ingredientSelect.value = '';
        quantityInput.value = '';

        // Add event listener for the remove button
        row.querySelector('.remove-ingredient').addEventListener('click', function() {
            row.remove();
        });
    });
});

