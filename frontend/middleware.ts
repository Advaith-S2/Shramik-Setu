// middleware.ts — ShramikSetu Next.js
// i18n routing + auth route protection
// Full implementation: Day 2 (Auth) + Day 11 (i18n)
// Today: just exports config so Next.js knows which paths to handle

import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

// Supported locales — must match locales/ JSON files and PRD §13 (M-13)
export const locales = ["en", "hi", "mr"] as const;
export type Locale = (typeof locales)[number];
export const defaultLocale: Locale = "en";

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // Skip static files and Next.js internals
  if (
    pathname.startsWith("/_next") ||
    pathname.startsWith("/api") ||
    pathname.includes(".")
  ) {
    return NextResponse.next();
  }

  // TODO (Day 2): check auth cookie → redirect to /[locale]/login if missing
  // TODO (Day 11): detect Accept-Language, redirect / to /[locale]/

  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
