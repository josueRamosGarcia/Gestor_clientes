CREATE TABLE estatus_clientes (
    ec_id       SERIAL PRIMARY KEY,
    ec_nombre   VARCHAR(32) NOT NULL
);

CREATE TABLE correos (
    corr_id             SERIAL PRIMARY KEY,
    corr_nombre         VARCHAR(64) NOT NULL UNIQUE,
    corr_contraseña     VARCHAR(256),
    corr_localizacion   VARCHAR(64)
);

CREATE TABLE clientes (
    cte_id          SERIAL PRIMARY KEY,
    cte_nombre      VARCHAR(64) NOT NULL,
    cte_apellidos   VARCHAR(64) NOT NULL,
    cte_curp        CHAR(18) NOT NULL UNIQUE,
    cte_nss         CHAR(11) NOT NULL UNIQUE,
    cte_rfc         CHAR(13) UNIQUE,
    ec_id           INTEGER NOT NULL,
    corr_id         INTEGER UNIQUE,
    FOREIGN KEY (ec_id) REFERENCES estatus_clientes(ec_id),
    FOREIGN KEY (corr_id) REFERENCES correos(corr_id)
);

CREATE TABLE telefonos (
    tel_id          SERIAL PRIMARY KEY,
    tel_telefono    VARCHAR(10) NOT NULL,
    tel_nombre      VARCHAR(128) NOT NULL,
    tel_parentesco  VARCHAR(64) NOT NULL,
    cte_id          INTEGER NOT NULL,
    FOREIGN KEY (cte_id) REFERENCES clientes(cte_id)
);

CREATE TABLE estatus_prestamos (
    ep_id       SERIAL PRIMARY KEY,
    ep_nombre   VARCHAR(32) NOT NULL
);

CREATE TABLE tipos_prestamos (
    tp_id       SERIAL PRIMARY KEY,
    tp_nombre   VARCHAR(32) NOT NULL
);

CREATE TABLE prestamos (
    prst_id         SERIAL PRIMARY KEY,
    prst_financiera VARCHAR(32) NOT NULL,
    prst_cat        DECIMAL(5,2) NOT NULL,
    prst_monto      DECIMAL(8,2) NOT NULL,
    prst_descuento  DECIMAL(7,2) NOT NULL,
    prst_plazo      INTEGER NOT NULL,
    prst_imp_pagar  DECIMAL(8,2) NOT NULL,
    prst_f_p_desc   DATE NOT NULL,
    prst_id_liq     INTEGER,
    cte_id          INTEGER NOT NULL,
    tp_id           INTEGER NOT NULL,
    ep_id           INTEGER NOT NULL,
    FOREIGN KEY (prst_id_liq) REFERENCES prestamos(prst_id),
    FOREIGN KEY (cte_id) REFERENCES clientes(cte_id),
    FOREIGN KEY (tp_id) REFERENCES tipos_prestamos(tp_id),
    FOREIGN KEY (ep_id) REFERENCES estatus_prestamos(ep_id)
);

CREATE TABLE usuarios (
    usr_id          SERIAL PRIMARY KEY,
    usr_nombre      VARCHAR(64) NOT NULL,
    usr_username    VARCHAR(32) NOT NULL UNIQUE,
    usr_pass        VARCHAR(256) NOT NULL,
    usr_activo      BOOLEAN DEFAULT TRUE
);

CREATE TABLE operaciones_auditoria (
    op_id SERIAL PRIMARY KEY,
    op_nombre VARCHAR(32) NOT NULL
);

CREATE TABLE eventos_auditoria (
    adt_id      SERIAL PRIMARY KEY,
    adt_tabla   VARCHAR(64) NOT NULL,
    adt_fecha   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    adt_dat_ant JSONB,
    adt_dat_des JSONB,
    adt_ip      VARCHAR(45) NOT NULL,
    op_id       INTEGER NOT NULL,
    usr_id      INTEGER NOT NULL,
    FOREIGN KEY (usr_id) REFERENCES usuarios(usr_id),
    FOREIGN KEY (op_id) REFERENCES operaciones_auditoria (op_id)
);

CREATE TABLE tipos_archivos (
    ta_id       SERIAL PRIMARY KEY,
    ta_nombre   VARCHAR(32) NOT NULL
);

CREATE TABLE archivos (
    arch_id         SERIAL PRIMARY KEY,
    arch_url        TEXT NOT NULL,
    arch_nombre     VARCHAR(64) NOT NULL,
    arch_f_subida   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ta_id           INTEGER NOT NULL,
    cte_id          INTEGER NOT NULL,
    FOREIGN KEY (ta_id) REFERENCES tipos_archivos (ta_id),
    FOREIGN KEY (cte_id) REFERENCES clientes (cte_id)
);
