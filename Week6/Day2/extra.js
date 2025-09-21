// 🔹 JWT Token Authentication in DRF
// 1. Normal Token Authentication (built-in DRF)
// When user logs in → server creates a token (random string).
// This token is stored in DB (Token table).
// Client sends this token in the Authorization header for every request.
// Problem: Server must look up token in DB every time → slow for large scale.

// 👉 Example header:
// Authorization: Token 3fcd02a9e7a5...

// 2. JWT Authentication (JSON Web Token)
// When user logs in → server creates a JWT token.
// JWT has 3 parts: Header.Payload.Signatur
// Header = type + algorithm
// Payload = user info (id, username, expiry)
// Signature = secure key to prevent tampering
// Token is self-contained → no DB lookup needed!
// Client sends JWT in header.
// Server only decodes & verifies signature.

// 👉 Example header:
// Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...

// ⚖️ Key Differences
// Feature	DRF Token Auth 🔑	JWT Auth 🔐
// Token stored in DB?	✅ Yes	❌ No (self-contained)
// Lookup on every request	✅ DB hit required	❌ Just decode token
// Expiry / Refresh	❌ Not built-in	✅ Built-in (short access token + long refresh token)
// Scalability	❌ Hard for big apps	✅ Best for large APIs (stateless)
// Security risk	Token in DB → revoke anytime	JWT valid until expiry (can’t revoke easily)
// ✅ Example Flow (JWT)

// User logs in → gets Access Token + Refresh Token.
// Client sends Access Token in each request.
// When Access Token expires → client uses Refresh Token to get a new one.
// 📌 Shortcut memory rule:
// Token Auth = stored in DB
// JWT = stored in token itself (stateless)

// 1. REST
// REST stands for REpresentational State Transfer.
// It’s an architecture style for designing networked applications.
// It uses HTTP methods like GET, POST, PUT, DELETE.
// REST APIs are stateless — server doesn’t keep user session information between requests.


// SOAP stands for Simple Object Access Protocol.
// It is a protocol (not just a style like REST) used for exchanging structured information between computers over a network.


// | Feature    | Django Form              | DRF Serializer               |
// | ---------- | ------------------------ | ---------------------------- |
// | Purpose    | Handle web form input    | Handle API JSON input/output |
// | Output     | Python objects / HTML    | JSON / Python objects        |
// | Used in    | Web pages                | APIs                         |
// | Validation | Validates form fields    | Validates JSON data          |
// | Rendering  | Can render HTML directly | Cannot render HTML           |
