-- Client tables
CREATE TABLE client_status (
    cs_id   SERIAL PRIMARY KEY,
    cs_name VARCHAR(32) NOT NULL
);

CREATE TABLE emails (
    em_id       SERIAL PRIMARY KEY,
    em_name     VARCHAR(64) NOT NULL UNIQUE,
    em_password VARCHAR(256),
    em_location VARCHAR(64)
);

CREATE TABLE clients (
    cl_id       SERIAL PRIMARY KEY,
    cl_name     VARCHAR(64) NOT NULL,
    cl_lname    VARCHAR(64) NOT NULL,
    cl_curp     CHAR(18) NOT NULL UNIQUE,
    cl_nss      CHAR(11) NOT NULL UNIQUE,
    cl_rfc      CHAR(13) NOT NULL UNIQUE,
    cs_id       INTEGER NOT NULL,
    em_id       INTEGER UNIQUE,
    FOREIGN KEY (cs_id) REFERENCES client_status (cs_id),
    FOREIGN KEY (em_id) REFERENCES emails (em_id)
);

CREATE TABLE phone_numbers (
    ph_id       SERIAL PRIMARY KEY,
    ph_number   CHAR(10) NOT NULL,
    ph_name     VARCHAR(128) NOT NULL,
    ph_rel      VARCHAR(64) NOT NULL,
    cl_id       INTEGER NOT NULL,
    FOREIGN KEY (cl_id) REFERENCES clients (cl_id) 
);

-- Loan tables
CREATE TABLE financial_institutions  (
    fi_id   SERIAL PRIMARY KEY,
    fi_name VARCHAR(32) NOT NULL
);

CREATE TABLE loan_status (
    ls_id   SERIAL PRIMARY KEY,
    ls_name VARCHAR(32) NOT NULL
);

CREATE TABLE loan_types (
    lt_id   SERIAL PRIMARY KEY,
    lt_name VARCHAR(32) NOT NULL
);

CREATE TABLE loans (
    ln_id           SERIAL PRIMARY KEY,
    ln_cat          DECIMAL(5,2) NOT NULL,
    ln_amount       DECIMAL(8,2) NOT NULL,
    ln_discount     DECIMAL(7,2) NOT NULL,
    ln_term         INTEGER NOT NULL,
    ln_am_pay       DECIMAL(8,2) NOT NULL,
    ln_f_disc_dt    DATE NOT NULL,
    ln_liq_id       INTEGER,
    cl_id           INTEGER NOT NULL,
    fi_id           INTEGER NOT NULL,
    ls_id           INTEGER NOT NULL,
    lt_id           INTEGER NOT NULL,
    FOREIGN KEY (cl_id) REFERENCES clients (cl_id),
    FOREIGN KEY (fi_id) REFERENCES financial_institutions (fi_id),
    FOREIGN KEY (ls_id) REFERENCES loan_status (ls_id),
    FOREIGN KEY (lt_id) REFERENCES loan_types (lt_id)
);

-- Files tables
CREATE TABLE file_types (
    ft_id   SERIAL PRIMARY KEY,
    ft_name VARCHAR(32) NOT NULL
);

CREATE TABLE files (
    fil_id      SERIAL PRIMARY KEY,
    fil_url     TEXT NOT NULL,
    fil_name    VARCHAR(64) NOT NULL,
    fil_up_dt   DATE DEFAULT CURRENT_TIMESTAMP,
    ft_id       INTEGER NOT NULL,
    cl_id       INTEGER NOT NULL,
    FOREIGN KEY (ft_id) REFERENCES file_types (ft_id),
    FOREIGN KEY (cl_id) REFERENCES clients (cl_id)
);

-- User tables
CREATE TABLE users (
    usr_id          SERIAL PRIMARY KEY,
    usr_name        VARCHAR(64) NOT NULL,
    usr_username    VARCHAR(32) NOT NULL UNIQUE,
    usr_password    VARCHAR(256) NOT NULL,
    usr_is_active   BOOLEAN DEFAULT TRUE
);

-- Audit tables
CREATE TABLE audit_operations (
    op_id   SERIAL PRIMARY KEY,
    op_name VARCHAR(32) NOT NULL
);

CREATE TABLE audit_events (
    ev_id       SERIAL PRIMARY KEY,
    ev_table    VARCHAR(64) NOT NULL,
    ev_date     TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ev_bef_data JSONB,
    ev_aft_data JSONB,
    ev_ip       VARCHAR(45) NOT NULL,
    op_id       INTEGER NOT NULL,
    usr_id      INTEGER NOT NULL,
    FOREIGN KEY (op_id) REFERENCES audit_operations (op_id),
    FOREIGN KEY (usr_id) REFERENCES users (usr_id)
);