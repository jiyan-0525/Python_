import time

def ft_tqdm(lst: range):
    total = len(lst)
    bar_len = 60
    
    for i, item in enumerate(lst):
        current = i + 1
        percent = int(current / total * 100)
        
        filled = int(bar_len * current / total)
        if filled > 0:
            bar = '=' * (filled - 1) + '>'
        else:
            bar = ''
        bar = bar.ljust(bar_len, ' ')
        
        print(f"\r{percent}% [{bar}] {current}/{total}", end='', flush=True)
        
        yield item