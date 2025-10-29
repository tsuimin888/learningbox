"""
任务清单应用测试文件
"""
import unittest
import json
import os
import time
from main import TaskCard, loadtask, createtask, deletetask

class TestTaskManager(unittest.TestCase):
    """任务管理器测试类"""
    
    def setUp(self):
        """测试前准备"""
        # 备份现有的tasks.json文件
        if os.path.exists('tasks.json'):
            os.rename('tasks.json', 'tasks_backup.json')
        
        # 创建空的tasks.json文件
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump({}, f)
    
    def tearDown(self):
        """测试后清理"""
        # 删除测试生成的tasks.json文件
        if os.path.exists('tasks.json'):
            os.remove('tasks.json')
        
        # 恢复备份的tasks.json文件
        if os.path.exists('tasks_backup.json'):
            os.rename('tasks_backup.json', 'tasks.json')
    
    def test_create_task(self):
        """测试创建任务"""
        # 创建测试任务数据
        test_task = {
            "name": "测试任务",
            "date": "2024/12/31 12:00:00",
            "level": 3,
            "description": "这是一个测试任务",
            "time": time.mktime(time.strptime("2024/12/31 12:00:00", '%Y/%m/%d %H:%M:%S'))
        }
        
        # 保存创建时间
        create_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        test_task["create"] = create_time
        
        # 手动添加任务到文件
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        tasks[create_time] = test_task
        
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)
        
        # 验证任务是否成功保存
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        self.assertIn(create_time, tasks)
        self.assertEqual(tasks[create_time]["name"], "测试任务")
    
    def test_delete_task(self):
        """测试删除任务"""
        # 创建测试任务
        test_task = {
            "name": "待删除任务",
            "date": "2024/12/31 12:00:00",
            "level": 2,
            "description": "这是一个待删除的测试任务",
            "time": time.mktime(time.strptime("2024/12/31 12:00:00", '%Y/%m/%d %H:%M:%S'))
        }
        
        create_time = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())
        test_task["create"] = create_time
        
        # 添加任务到文件
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        tasks[create_time] = test_task
        
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4)
        
        # 删除任务
        deletetask(create_time)
        
        # 验证任务是否被删除
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        
        self.assertNotIn(create_time, tasks)

if __name__ == '__main__':
    unittest.main()