# BIASAKAN BACA DULU !!! INI STEP KALIAN UNTUK BISA BIKIN KONEKSI KE DATABASE 

## MASUKIN DATA ENV KALIAN 

### MYSQL

```Powershell
DATABASE_HOST=nama host kalian
DATABASE_USER=nama user kalian
DATABASE_PASSWORD= pass database kalian
DATABASE_NAME=nama database kalian
DATABASE_PORT= PORT kalian
```

### POSTGRES

```Powershell
DATABASE_URL=postgresql://USERNAME_DATABASE_KALIAN:PASSWORD_DATABASE_KALIAN@HOST_DATABASE_KALIAN(LOCALHOST BIASANYA):PORT_KALIAN/NAMA_DATABASE_KALIAN
```

### dependencies yang dibutuhin 

1. FLASK
```bash
uv add flask
```
2. PSYCOPG2
```bash
uv add psycopg2
```
3. FLASK-SQLALCHEMY
```bash
uv add flask-sqlalchemy
```
4. PYTHON-DOTENV
```bash
uv add python-dotenv
```
### PASTIIN SEMUA SUDAH MASUK KE DEPENDENCIES KALIAN

![alt text](app/assets/image.png)

### KALAU UDA BERJALAN PASTI ADA KONFIRMASI KALAU KALIAN SUDAH TERKONEKSI KE DATABASE MASING2

![alt text](app/assets/image-1.png)

