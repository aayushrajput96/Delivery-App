import React, { useState } from 'react';

const CreateOrder = () => {
  const [deliveryAddress, setDeliveryAddress] = useState('');
  const [totalAmount, setTotalAmount] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const token = localStorage.getItem('access_token');
    const response = await fetch('http://127.0.0.1:8000/api/orders/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({
        delivery_address: deliveryAddress,
        total_amount: totalAmount,
      }),
    });

    const data = await response.json();
    if (response.ok) {
      alert('Order placed successfully');
    } else {
      alert('Error placing order');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Delivery Address"
        value={deliveryAddress}
        onChange={(e) => setDeliveryAddress(e.target.value)}
      />
      <input
        type="number"
        placeholder="Total Amount"
        value={totalAmount}
        onChange={(e) => setTotalAmount(e.target.value)}
      />
      <button type="submit">Place Order</button>
    </form>
  );
};

export default CreateOrder;
