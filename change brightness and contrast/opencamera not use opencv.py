from typing import Optional

import av
from PIL.Image import Image, logger


def take_photo_from_video_source(video_url: str, rtsp_transport: str) -> Optional[Image]:
    video_options = {
        'rtsp_transport': rtsp_transport,
        'pix_fmts': 'yuv420p|rgb24|yuv444p',
    }
    try:
        container = av.open(video_url, options=video_options)
    except av.AVError as e:
        logger.error("IP Camera is not online. Error {}", e)
        return
    frame = next(container.decode(video=0))
    return frame.to_image()
