#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Merhaba, \n\nBu bir Telegram <b>Video Sıkıştırma Botudur</b>. \n\n<b>Lütfen bana herhangi bir büyük Telegram dosyası gönderin, onu küçük video dosyası olarak sıkıştıracağım!</b> \n\nDaha fazla ayrıntı için /help \n\nSupport Group: @trbotlarsohbet"
   
    ABS_TEXT = " Lütfen bencil olma."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "📥 İndiriliyor ... 📥 \n"
    
    UPLOAD_START = "📤 Yükleniyor ... 📤 \n"
    
    COMPRESS_START = "📀 Sıkıştırılıyor ... 📀"
    
    RCHD_BOT_API_LIMIT = "İzin verilen max boyut (50MB). Yine de yüklemeye çalışıyorum."
    
    RCHD_TG_API_LIMIT = "İndiriildi {} saniyede.\nAlgılanan DOSYALAR: {}\nÜzgünüm Telegram 1.95GB API kısıtlaması sebebiyle işlemi gerçekleştiremiyorum."
    
    COMPRESS_SUCCESS = "📥 İndirildi {}\n\n📀 Sıkıştırıldı {}\n\n📤 Yüklendi {}\n\nBy @trbotlar"

    COMPRESS_PROGRESS = "⏳ ETA: {}\n🚀 İşleniyor: {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Özel video / dosya küçük resmi kaydedildi. Bu görüntü video / dosyanızda kullanılacak."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Thumbnail başarıyla silindi."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media başarıyla silindi."
    
    SAVED_RECVD_DOC_FILE = "✅ İndirme başarılı."
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "Thumbnail bulunamadı."
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Updates Channel."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Merhaba, ben Video Sıkıştırma Botuyum \n\n1. Bana büyük telegram dosyanızı gönderin \n2. Şu şekilde yanıtlayın: `/compress 50` \n\nDestek Grubu: @trbotlarsohbet"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
