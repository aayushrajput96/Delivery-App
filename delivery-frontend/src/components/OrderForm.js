import React, { useState } from 'react';
import axios from 'axios';

const OrderForm = () => {
  const [item, setItem] = useState('');
  const [quantity, setQuantity] = useState(1);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('token');
    try {
      await axios.post('http://127.0.0.1:8000/api/orders/', { item, quantity }, {
        headers: { Authorization: `Token ${token}` }
      });
      alert('Order created successfully!');
    } catch (err) {
      alert('Failed to create order');
    }
  };

  return (
    <div>
      <h2>Create Order</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" value={item} onChange={(e) => setItem(e.target.value)} placeholder="Item" />
        <input type="number" value={quantity} onChange={(e) => setQuantity(e.target.value)} placeholder="Quantity" />
        <button type="submit">Create Order</button>
      </form>
    </div>
  );
};

export default OrderForm;
