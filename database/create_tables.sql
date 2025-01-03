-- -- Products Table
-- CREATE TABLE products (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     barcode VARCHAR(50) UNIQUE NOT NULL,
--     description TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Inventory Table
-- CREATE TABLE inventory (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     product_id INT NOT NULL,
--     location ENUM('manufacturing', 'warehouse', 'loading_area') NOT NULL,
--     quantity INT DEFAULT 0,
--     FOREIGN KEY (product_id) REFERENCES products(id)
-- );

-- -- Orders Table
-- CREATE TABLE orders (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     product_id INT NOT NULL,
--     quantity INT NOT NULL,
--     status ENUM('pending', 'fulfilled', 'in_production') DEFAULT 'pending',
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (product_id) REFERENCES products(id)
-- );

-- -- Notifications Table
-- CREATE TABLE notifications (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     message TEXT NOT NULL,
--     is_read BOOLEAN DEFAULT FALSE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );


-- CREATE TABLE users (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(100) NOT NULL UNIQUE,
--     password-hash VARCHAR(255) NOT NULL, -- Passwords should be hashed
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );


-- Products Table
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Automatically incrementing ID
    name VARCHAR(100) NOT NULL,                         -- Product name cannot be null
    barcode VARCHAR(50) UNIQUE NOT NULL,                -- Barcode is unique and cannot be null
    description TEXT,                                   -- Description is optional
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Automatically set the timestamp for creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Track updates
    INDEX(name)                                         -- Index on name for faster search
);

-- Inventory Table
CREATE TABLE inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Automatically incrementing ID
    product_id INT NOT NULL,                            -- Foreign key for product
    location ENUM('manufacturing', 'warehouse', 'loading_area') NOT NULL,  -- Location in inventory
    quantity INT DEFAULT 0,                             -- Default quantity is 0
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when entry is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Track updates
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE, -- Cascade delete if product is deleted
    INDEX(product_id, location)                        -- Index for product_id and location for faster lookups
);

-- Orders Table
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Automatically incrementing ID
    product_id INT NOT NULL,                            -- Foreign key for product
    quantity INT NOT NULL,                              -- Quantity ordered
    status ENUM('pending', 'fulfilled', 'in_production') DEFAULT 'pending', -- Order status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when order is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Track updates
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE, -- Cascade delete if product is deleted
    INDEX(product_id, status)                          -- Index for product_id and status for fast query filtering
);

-- Notifications Table
CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Automatically incrementing ID
    message TEXT NOT NULL,                              -- Notification message cannot be null
    is_read BOOLEAN DEFAULT FALSE,                      -- Default to unread
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when notification is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Track updates
);

-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,                 -- Automatically incrementing ID
    username VARCHAR(100) NOT NULL UNIQUE,              -- Username must be unique
    password_hash VARCHAR(255) NOT NULL,                -- Password hash cannot be null (Note: password-hash corrected to password_hash)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp for when user is created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Track updates
    INDEX(username)                                    -- Index on username for fast login query
);


ALTER TABLE inventory ADD CONSTRAINT chk_quantity CHECK (quantity >= 0);

