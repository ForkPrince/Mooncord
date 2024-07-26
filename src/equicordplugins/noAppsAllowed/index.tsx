/*
 * Vencord, a Discord client mod
 * Copyright (c) 2023 Vendicated and contributors
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

import { migratePluginSettings } from "@api/Settings";
import { EquicordDevs } from "@utils/constants";
import definePlugin from "@utils/types";

migratePluginSettings("NoAppsAllowed", "noAppsAllowed");
export default definePlugin({
    name: "NoAppsAllowed",
    description: "returns the bot's tag :skulk:",
    authors: [EquicordDevs.kvba],

    patches: [
        {
            find: ",APP_TAG:\"",
            replacement: {
                match: /APP_TAG:".*?"/,
                replace: "APP_TAG:\"BOT\""
            }
        }
    ],

});
