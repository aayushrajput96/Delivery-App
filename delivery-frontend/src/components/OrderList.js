import React, { useEffect, useState } from 'react';
import api from '../api';

const OrderList = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    api.get('/orders/').then((response) => {
      setOrders(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Order List</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            {order.pickup_address} to {order.dropoff_address} - {order.status}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default OrderList;
