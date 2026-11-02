"""验证路由、独立安装引用和公共资料副本；不模拟 AI 的实际推理。"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
LINK = re.compile(r'\]\(([^)]+)\)')

class RepositoryChecks(unittest.TestCase):
    def test_router_lists_every_specialist_once(self):
        router = (ROOT / 'SKILL.md').read_text(encoding='utf-8-sig')
        for skill in sorted(SKILLS.iterdir()):
            if skill.is_dir():
                with self.subTest(skill=skill.name):
                    self.assertEqual(router.count(f'skills/{skill.name}/SKILL.md'), 1)
                    self.assertTrue((skill / 'SKILL.md').is_file())

    def test_local_links_work_in_each_skill(self):
        files = [ROOT / 'SKILL.md', ROOT / 'README.md', ROOT / 'README.zh-CN.md']
        files.extend(SKILLS.glob('*/SKILL.md'))
        for file in files:
            for link in LINK.findall(file.read_text(encoding='utf-8-sig')):
                if '://' in link or link.startswith('#'):
                    continue
                with self.subTest(file=str(file.relative_to(ROOT)), link=link):
                    self.assertTrue((file.parent / link.split('#')[0]).is_file())
                    # 单独复制专项目录后，引用仍须保持在该专项目录内。
                    if file.parent.parent == SKILLS:
                        self.assertTrue((file.parent / link.split('#')[0]).resolve().is_relative_to(file.parent.resolve()))

    def test_reference_copies_match_authoritative_files(self):
        for copy in SKILLS.glob('*/references/*.md'):
            source = ROOT / 'references' / copy.name
            with self.subTest(copy=str(copy.relative_to(ROOT))):
                self.assertTrue(source.is_file())
                self.assertEqual(copy.read_bytes(), source.read_bytes())

    def test_expected_scenario_coverage_is_routed(self):
        # 固定场景检查入口与参考文件是否存在；不声称已测试模型行为。
        scenarios = {
            '笔记本不充电': ['laptop-repair', 'power-charging-diagnostics'],
            '显卡花屏': ['gpu-repair', 'repair-document-research'],
            '硬盘异响且数据重要': ['storage-data-triage'],
            '洗衣机不排水': ['washing-machine-repair'],
            '空调不制冷': ['air-conditioner-repair'],
            '示波器地夹': ['oscilloscope-diagnostics'],
        }
        router = (ROOT / 'SKILL.md').read_text(encoding='utf-8-sig')
        for scenario, required in scenarios.items():
            for name in required:
                with self.subTest(scenario=scenario, skill=name):
                    self.assertIn(f'skills/{name}/SKILL.md', router)
                    self.assertTrue((SKILLS / name / 'SKILL.md').is_file())

if __name__ == '__main__':
    unittest.main(verbosity=2)
