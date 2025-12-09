"""Tools for Difficulty Tester Agent"""


def exit_loop():
    """當謎語達到理想難度時呼叫此函式，結束迭代循環。
    
    返回一個明確的完成訊息。
    這個訊息會被設置為 difficulty_feedback，讓後續的 agent 知道已經完成。
    
    Returns:
        str: 完成訊息，標記循環應該結束
    """
    print("\n" + "="*60)
    print("🎉 [達標] 謎語難度適中，結束迭代循環")
    print("="*60 + "\n")
    
    return "✅ 循環完成：謎語難度已達標，無需繼續改進。"

