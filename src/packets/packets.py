packets: dict = {
    "1": "IDLogin",
    "2": "IDPlayStatus",
    "3": "IDServerToClientHandshake",
    "4": "IDClientToServerHandshake",
    "5": "IDDisconnect",
    "6": "IDResourcePacksInfo",
    "7": "IDResourcePackStack",
    "8": "IDResourcePackClientResponse",
    "9": "IDText",
    "10": "IDSetTime",
    "11": "IDStartGame",
    "12": "IDAddPlayer",
    "13": "IDAddActor",
    "14": "_",
    "15": "IDRemoveActor",
    "16": "IDAddItemActor",
    "17": "IDTakeItemActor",
    "18": "IDMoveActorAbsolute",
    "19": "IDMovePlayer",
    "20": "IDPassengerJump",
    "21": "IDUpdateBlock",
    "22": "IDAddPainting",
    "23": "IDTickSync",
    "24": "_",
    "25": "IDLevelEvent",
    "26": "IDBlockEvent",
    "27": "IDActorEvent",
    "28": "IDMobEffect",
    "29": "IDUpdateAttributes",
    "30": "IDInventoryTransaction",
    "31": "IDMobEquipment",
    "32": "IDMobArmourEquipment",
    "33": "IDInteract",
    "34": "IDBlockPickRequest",
    "35": "IDActorPickRequest",
    "36": "IDPlayerAction",
    "37": "_",
    "38": "IDHurtArmour",
    "39": "IDSetActorData",
    "40": "IDSetActorMotion",
    "41": "IDSetActorLink",
    "42": "IDSetHealth",
    "43": "IDSetSpawnPosition",
    "44": "IDAnimate",
    "45": "IDRespawn",
    "46": "IDContainerOpen",
    "47": "IDContainerClose",
    "48": "IDPlayerHotBar",
    "49": "IDInventoryContent",
    "50": "IDInventorySlot",
    "51": "IDContainerSetData",
    "52": "IDCraftingData",
    "53": "IDCraftingEvent",
    "54": "IDGUIDataPickItem",
    "55": "IDAdventureSettings",
    "56": "IDBlockActorData",
    "57": "IDPlayerInput",
    "58": "IDLevelChunk",
    "59": "IDSetCommandsEnabled",
    "60": "IDSetDifficulty",
    "61": "IDChangeDimension",
    "62": "IDSetPlayerGameType",
    "63": "IDPlayerList",
    "64": "IDSimpleEvent",
    "65": "IDEvent",
    "66": "IDSpawnExperienceOrb",
    "67": "IDClientBoundMapItemData",
    "68": "IDMapInfoRequest",
    "69": "IDRequestChunkRadius",
    "70": "IDChunkRadiusUpdated",
    "71": "IDItemFrameDropItem",
    "72": "IDGameRulesChanged",
    "73": "IDCamera",
    "74": "IDBossEvent",
    "75": "IDShowCredits",
    "76": "IDAvailableCommands",
    "77": "IDCommandRequest",
    "78": "IDCommandBlockUpdate",
    "79": "IDCommandOutput",
    "80": "IDUpdateTrade",
    "81": "IDUpdateEquip",
    "82": "IDResourcePackDataInfo",
    "83": "IDResourcePackChunkData",
    "84": "IDResourcePackChunkRequest",
    "85": "IDTransfer",
    "86": "IDPlaySound",
    "87": "IDStopSound",
    "88": "IDSetTitle",
    "89": "IDAddBehaviourTree",
    "90": "IDStructureBlockUpdate",
    "91": "IDShowStoreOffer",
    "92": "IDPurchaseReceipt",
    "93": "IDPlayerSkin",
    "94": "IDSubClientLogin",
    "95": "IDAutomationClientConnect",
    "96": "IDSetLastHurtBy",
    "97": "IDBookEdit",
    "98": "IDNPCRequest",
    "99": "IDPhotoTransfer",
    "100": "IDModalFormRequest",
    "101": "IDModalFormResponse",
    "102": "IDServerSettingsRequest",
    "103": "IDServerSettingsResponse",
    "104": "IDShowProfile",
    "105": "IDSetDefaultGameType",
    "106": "IDRemoveObjective",
    "107": "IDSetDisplayObjective",
    "108": "IDSetScore",
    "109": "IDLabTable",
    "110": "IDUpdateBlockSynced",
    "111": "IDMoveActorDelta",
    "112": "IDSetScoreboardIdentity",
    "113": "IDSetLocalPlayerAsInitialised",
    "114": "IDUpdateSoftEnum",
    "115": "IDNetworkStackLatency",
    "116": "_",
    "117": "IDScriptCustomEvent",
    "118": "IDSpawnParticleEffect",
    "119": "IDAvailableActorIdentifiers",
    "120": "_",
    "121": "IDNetworkChunkPublisherUpdate",
    "122": "IDBiomeDefinitionList",
    "123": "IDLevelSoundEvent",
    "124": "IDLevelEventGeneric",
    "125": "IDLecternUpdate",
    "126": "_",
    "127": "IDAddEntity",
    "128": "IDRemoveEntity",
    "129": "IDClientCacheStatus",
    "130": "IDMapCreateLockedCopy",
    "131": "IDOnScreenTextureAnimation",
    "132": "IDStructureTemplateDataRequest",
    "133": "IDStructureTemplateDataResponse",
    "134": "_",
    "135": "IDClientCacheBlobStatus",
    "136": "IDClientCacheMissResponse",
    "137": "IDEducationSettings",
    "138": "IDEmote",
    "139": "IDMultiPlayerSettings",
    "140": "IDSettingsCommand",
    "141": "IDAnvilDamage",
    "142": "IDCompletedUsingItem",
    "143": "IDNetworkSettings",
    "144": "IDPlayerAuthInput",
    "145": "IDCreativeContent",
    "146": "IDPlayerEnchantOptions",
    "147": "IDItemStackRequest",
    "148": "IDItemStackResponse",
    "149": "IDPlayerArmourDamage",
    "150": "IDCodeBuilder",
    "151": "IDUpdatePlayerGameType",
    "152": "IDEmoteList",
    "153": "IDPositionTrackingDBServerBroadcast",
    "154": "IDPositionTrackingDBClientRequest",
    "155": "IDDebugInfo",
    "156": "IDPacketViolationWarning",
    "157": "IDMotionPredictionHints",
    "158": "IDAnimateEntity",
    "159": "IDCameraShake",
    "160": "IDPlayerFog",
    "161": "IDCorrectPlayerMovePrediction",
    "162": "IDItemComponent",
    "163": "IDFilterText",
    "164": "IDClientBoundDebugRenderer",
    "165": "IDSyncActorProperty",
    "166": "IDAddVolumeEntity",
    "167": "IDRemoveVolumeEntity",
    "168": "IDSimulationType",
    "169": "IDNPCDialogue",
    "170": "IDEducationResourceURI",
    "171": "IDCreatePhoto",
    "172": "IDUpdateSubChunkBlocks",
    "173": "IDPhotoInfoRequest",
    "174": "IDSubChunk",
    "175": "IDSubChunkRequest",
    "176": "IDClientStartItemCooldown",
    "177": "IDScriptMessage",
    "178": "IDCodeBuilderSource"
}