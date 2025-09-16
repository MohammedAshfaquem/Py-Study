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