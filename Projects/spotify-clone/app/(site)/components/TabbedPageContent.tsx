"use client";

import Link from "next/link";
import PageContent from "./PageContent";
import { Song } from "@/types";
import { twMerge } from "tailwind-merge";

interface TabbedPageContentProps {
    songs: Song[];
    currentTab: string;
}

// Массив с данными для табов
const TABS = [
    { name: "Newest", value: "created_at" },
    { name: "Popular", value: "title" },
    { name: "Author", value: "author" },
];

const TabbedPageContent: React.FC<TabbedPageContentProps> = ({ songs, currentTab }) => {
    return (
        <div>
            <div className="flex gap-4 pb-2">
                {TABS.map((tab) => (
                    <Link
                        key={tab.value}
                        onClick={() => {console.log(currentTab)}}
                        href={`/?tab=${tab.value}`}
                        className={
                            twMerge(`
                                px-4 py-2 text-md font-medium
                                ${currentTab === tab.value
                                    ? "text-blue-500 border-b-2 border-blue-500 font-semibold"
                                    : "text-neutral-400 hover:text-white"}
                            `)
                        }
                        >
                        {tab.name}
                    </Link>
                ))}
            </div>
            <PageContent songs={songs} />
        </div>
    );
};

export default TabbedPageContent;