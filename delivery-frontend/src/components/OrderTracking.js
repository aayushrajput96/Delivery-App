import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderTracking = ({ orderId }) => {
  const [order, setOrder] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOrder = async () => {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/orders/${orderId}/`, {
          headers: { Authorization: `Token ${token}` }
        });
        setOrder(response.data);
        setLoading(false);
      } catch (err) {
        setError('Error fetching order');
        setLoading(false);
      }
    };

    fetchOrder();
  }, [orderId]);

  if (loading) {
    return <div>Loading order details...</div>;
  }

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      {order && (
        <div>
          <h2>Order Tracking</h2>
          <p>Order ID: {order.id}</p>
          <p>Item: {order.item}</p>
          <p>Delivery Address: {order.delivery_address}</p>
          <p>Total Amount: ${order.total_amount}</p>
          <p>Status: {order.status}</p>
          <p>Estimated Delivery Time: {order.delivery_time}</p>
        </div>
      )}
    </div>
  );
};

export default OrderTracking;
