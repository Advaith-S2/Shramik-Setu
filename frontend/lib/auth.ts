/**
 * lib/auth.ts — Auth helpers
 * Stub — implement in Day 2 (M-01) using Supabase Auth client.
 */

export type UserRole = "worker" | "supervisor" | "contractor" | "inspector" | "admin";

export interface AuthUser {
  id: string;
  email: string;
  full_name: string;
  role: UserRole;
}

/** Get the current authenticated user from stored JWT. Returns null if unauthenticated. */
export function getCurrentUser(): AuthUser | null {
  // TODO (Day 2): decode JWT from storage, return user payload
  return null;
}

/** Returns true if the user has one of the allowed roles. */
export function hasRole(user: AuthUser | null, ...roles: UserRole[]): boolean {
  if (!user) return false;
  return roles.includes(user.role);
}

/** Get the role-specific dashboard route for a user. */
export function getDashboardRoute(role: UserRole, locale = "en"): string {
  const routes: Record<UserRole, string> = {
    worker: `/${locale}/worker/dashboard`,
    supervisor: `/${locale}/supervisor/dashboard`,
    contractor: `/${locale}/contractor/dashboard`,
    inspector: `/${locale}/inspector/dashboard`,
    admin: `/${locale}/inspector/dashboard`, // Admin shares inspector dashboard for MVP
  };
  return routes[role];
}
