# API Scaffolder

Generate a complete REST API endpoint from a one-line description.

## Trigger

Use when the user says "create endpoint for X", "new API route", `/scaffold-api`, or describes a CRUD operation.

## Process

1. Ask: "What resource? What operations (GET/POST/PUT/DELETE)? What framework?"
2. If the user already specified everything, skip questions
3. Generate the route handler with:
   - Input validation
   - Error handling
   - Response format
   - TypeScript types (if applicable)
4. Show the code and ask: "Want me to add tests or adjust anything?"
5. If yes, generate test file alongside

## Constraints

- Match the project's existing patterns (check existing routes first)
- Don't add auth middleware unless asked
- Don't create database migrations — only the route layer
- Use the project's existing error format

## Output

One file per endpoint in the project's routes directory, following existing conventions.
