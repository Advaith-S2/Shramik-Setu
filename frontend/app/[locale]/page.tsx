// app/[locale]/page.tsx — Landing / Splash page
// PRD Screen #1: Logo, tagline, Login/Register CTAs, language selector
// Stub for Day 1 — visual implementation in Day 2

export default function LandingPage({
  params,
}: {
  params: { locale: string };
}) {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center bg-slate-50 p-8">
      <div className="text-center max-w-xl">
        <h1 className="text-4xl font-bold text-blue-900 mb-2">ShramikSetu</h1>
        <p className="text-slate-600 text-lg mb-8">
          Digital Employment &amp; Wage Verification Platform
          <br />
          <span className="text-sm text-slate-400">
            श्रमिक सेतु · श्रमिक सेतु
          </span>
        </p>
        <div className="flex gap-4 justify-center">
          <a
            href={`/${params.locale}/login`}
            className="px-6 py-3 bg-blue-800 text-white rounded-md font-medium hover:bg-blue-900 transition-colors"
          >
            Login
          </a>
          <a
            href={`/${params.locale}/register`}
            className="px-6 py-3 border border-blue-800 text-blue-800 rounded-md font-medium hover:bg-blue-50 transition-colors"
          >
            Register
          </a>
        </div>
        <p className="mt-8 text-xs text-slate-400">
          Locale: {params.locale} · Day 1 scaffold stub
        </p>
      </div>
    </main>
  );
}
