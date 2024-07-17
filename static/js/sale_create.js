document.addEventListener('DOMContentLoaded', function() {
    const orderSummary = document.getElementById('order-summary');
    const totalCostElement = document.getElementById('total-cost');
    let totalCost = 0;

    document.querySelectorAll('.add-to-order').forEach(button => {
        button.addEventListener('click', function() {
            const name = this.getAttribute('data-name');
            const cost = parseFloat(this.getAttribute('data-cost'));

            // Add item to order summary
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><input type="hidden" name="items[]" value="${name}">${name}</td>
                <td>$${cost.toFixed(2)}</td>
            `;
            orderSummary.appendChild(row);

            totalCost += cost;
            totalCostElement.textContent = `$${totalCost.toFixed(2)}`;
        });
    });

const checkoutButton = document.getElementById('submit-button');
  checkoutButton.addEventListener('click', function(event) {
      event.preventDefault();
      const items = Array.from(document.querySelectorAll('input[name="items[]"]')).map(input => input.value);
      const paymentMethod = document.querySelector('input[name="payment-method"]:checked').value;
      const isCard = (paymentMethod === 'card'); 
      const total = totalCost;

      console.log("Checkout button clicked");

      fetch(saleProcessUrl, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCookie('csrftoken'),
          },
          body: JSON.stringify({ items: items, is_card: isCard, total: total })
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              window.location.href = saleCreateUrl;
          } else {
               alert(data.error || 'Something went wrong. Please try again.');
          }
      })
      .catch(error => console.error('Error:', error));
  });

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
});

