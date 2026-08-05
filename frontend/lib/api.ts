/**
 * lib/api.ts — Axios API client wrapper
 * All API calls must go through this — never fetch() directly in components.
 * Base URL: NEXT_PUBLIC_API_URL (e.g. http://localhost:8000/api/v1)
 * Full implementation: Day 2 (add auth header injection after JWT is available)
 */
import axios from "axios";

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1",
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10_000,
});

// Request interceptor — inject JWT Bearer token
// TODO (Day 2): read token from httpOnly cookie or localStorage, attach to Authorization header
api.interceptors.request.use((config) => {
  // const token = getToken(); // implement in Day 2
  // if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Response interceptor — handle 401 globally
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // TODO (Day 2): clear stored token, redirect to /login
    }
    return Promise.reject(error);
  }
);

export default api;
