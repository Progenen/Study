import { Song } from "@/types";
import { createServerComponentClient } from "@supabase/auth-helpers-nextjs";
import { console } from "inspector";
import { cookies } from "next/headers";

const getSortSongs = async (sortType: string): Promise<Song[]> => {
    const supabase = createServerComponentClient({
        cookies: cookies
    });

    const { data, error } = await supabase
        .from('songs')
        .select('*')
        .order(sortType, { ascending: false })

    if (error) {
        console.log(error);
    }

    return (data as any) || []
}

export default getSortSongs;