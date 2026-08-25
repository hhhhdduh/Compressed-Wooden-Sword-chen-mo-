# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModPiy3Q2Mp", version="0.0.1")
class Script_NeteaseModPiy3Q2Mp(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModPiy3Q2MpServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModPiy3Q2MpServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModPiy3Q2MpClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModPiy3Q2MpClientDestroy(self):
        pass
