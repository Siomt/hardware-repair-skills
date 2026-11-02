"""将公共参考文件同步到需要单独安装的专项。"""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
for destination in (root / 'skills').glob('*/references/*.md'):
    source = root / 'references' / destination.name
    if not source.is_file():
        raise SystemExit(f'缺少公共参考文件: {source}')
    shutil.copyfile(source, destination)
    print(f'{source.relative_to(root)} -> {destination.relative_to(root)}')
