// app/[locale]/layout.tsx — Root locale layout
// Wraps all locale-specific pages with shared providers
// Full i18n implementation: Day 11 (M-13)
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "ShramikSetu — Digital Labour Welfare Platform",
  description:
    "Digital Employment, Wage Verification & Benefit Platform for India's Unorganised Workforce.",
};

export default function LocaleLayout({
  children,
}: {
  children: React.ReactNode;
  params: { locale: string };
}) {
  // TODO (Day 11): wrap with next-intl NextIntlClientProvider
  return <>{children}</>;
}

// Static params for the 3 supported locales
export async function generateStaticParams() {
  return [{ locale: "en" }, { locale: "hi" }, { locale: "mr" }];
}
