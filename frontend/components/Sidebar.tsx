"use client";
import Link from "next/link";
import { usePathname } from "next/navigation";

const links = [
  { href: "/", label: "Mission Control" },
  { href: "/assets", label: "Assets" },
  { href: "/findings", label: "Findings" },
  { href: "/attack-paths", label: "Attack Paths" },
  { href: "/threat-memory", label: "Threat Memory" },
  { href: "/reports", label: "Reports" },
  { href: "/lix", label: "Ask Lix" },
];

export default function Sidebar() {
  const pathname = usePathname();
  return (
    <aside className="sidebar">
      <div className="logo">LN1</div>
      <p className="tagline">Hunt the risk before it hunts you.</p>
      <nav>
        {links.map((l) => (
          <Link key={l.href} href={l.href}>
            <div className={pathname === l.href ? "active" : ""}>{l.label}</div>
          </Link>
        ))}
      </nav>
    </aside>
  );
}
