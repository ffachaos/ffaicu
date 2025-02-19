sub hissatu{
	if ($waza_ritu > int(rand(80 + $syukuhuku * 40))) {
		$item[1] += $item[1];
		$item[4] += $item[4];
		$syukuhuku++;
		$com1 .="<font class=\"white\" size=5>$chara[4]は祝福の歌を歌った♪（攻撃力、防御力増大、効果持続）</font><br>";
	}
}
sub atowaza{}
1;