import { useState } from "react";
import getSongs from "../../actions/getSongs";
import Header from "../../components/Header";
import ListItem from "../../components/ListItem";
import PageContent from "./components/PageContent";
import TabbedPageContent from "./components/TabbedPageContent";
import getSortSongs from "@/actions/getSortSongs";

export const revalidate = 0;

export default async function Home({ searchParams }: { searchParams: { tab?: string } }) {
  const currentTab = searchParams.tab || 'created_at';
  const songs = await getSortSongs(currentTab);
  
  return (
    <div className="
      bg-neutral-900
      rounded-lg
      h-full
      w-full
      overflow-hidden
      overflow-y-auto
    ">
      <Header>
        <div className="mb-2">
          <h1
            className="
              text-white
              text-3xl
              text-semibold
            "
          >
            Welcome back
          </h1>
        </div>
        <div 
          className="
            grid
            grid-cols-1
            sm:grid-cols-2
            xl:grid-cols-3
            2xl:grid-col-4
            gap-3
            mt-4
          ">
            <ListItem 
              image="/images/liked.jpeg"
              name="Liked Songs"
              href="liked"
            />
          </div>
      </Header>
      <div className="mt-2 mb-7 px-6">
        <TabbedPageContent songs={songs} currentTab={currentTab} />
      </div>
    </div>
  );
}
