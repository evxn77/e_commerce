# 🛒 E-SHOP: Django Multi-Role E-Commerce Platform

A robust, minimal, and fully functional e-commerce web application built with **Python** and **Django**. This platform features a dual-interface system: a sleek, modern storefront for customers and a comprehensive management dashboard for administrators.

---

## 🚀 Project Overview

This project is built using the **Django MVT (Model-View-Template)** architecture. It separates concerns into three distinct apps to ensure scalability and clean code:

* **`main_app`**: Handles the landing page, global styling, and navigation.
* **`users_app`**: Manages customer accounts, authentication, and the shopping/ordering process.
* **`admin_app`**: A dedicated portal for staff to manage inventory, users, and sales data.



---

## ✨ Key Features

### 👤 Customer Features
* **Dynamic Storefront:** Real-time product listing filtered by stock availability.
* **Secure Authentication:** User registration and login with smart-redirects based on user roles.
* **Checkout System:** Integrated order placement with inventory validation.
* **Order History:** A personalized dashboard for customers to track their purchase status (Pending/Shipped/Delivered).

### 🛠️ Administrative Features
* **Protected Management Portal:** Access-controlled dashboard using Django's `@user_passes_test` decorators.
* **Inventory CRUD:** Full Create, Read, Update, and Delete capabilities for products.
* **User Management:** Centralized view of all registered customers.
* **Stock Monitoring:** Automated stock alerts for low-inventory items.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.13+, Django 6.0
* **Frontend:** HTML5, CSS3 (Custom Grid/Flexbox system), Django Template Language (DTL)
* **Database:** SQLite3 (Default development database)



---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/e-shop-django.git](https://github.com/your-username/e-shop-django.git)
   cd e-shop-django
