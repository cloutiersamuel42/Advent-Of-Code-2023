
import java.io.File

class Card(val winning: List<Int>, val mine: List<Int>, val id: Int) {
    var matching = 0
    var points = countPoints()
    var copies = 1

    private fun countPoints(): Int {
        mine.forEach {
            winning.forEach { w ->
                if (w == it) {
                    matching++
                    when {
                        points == 0 -> points = 1
                        else -> points *= 2
                    }
                }
            }
        }
        return points
    }
}

fun main() {
    val content: List<String> = File("input.txt").readLines()

    val res1 = part1(content)
    val res2 = part2(content)

    println("Part 1: $res1")
    println("Part 2: $res2")
}

fun part1(lines: List<String>): Int {
    var id = 1
    var total = 0
    // iterate input lines
    lines.forEach {
        val cardInput = it.split(":")[1].split("|").map { str -> str.trim() }
        val winning: List<Int> = cardInput[0].split("\\s+".toRegex()).map { n -> n.toInt() }
        val mine: List<Int> = cardInput[1].split("\\s+".toRegex()).map { n -> n.toInt() }
        val card = Card(winning, mine, id)
        println("$id: This card has ${card.matching} matching values for ${card.points} points!")
        id++
        total += card.points
    }
    return total
}

fun part2(lines: List<String>): Int {
    var id = 1;
    val cards: MutableList<Card> = mutableListOf()
    // iterate input lines
    lines.forEach {
        val cardInput = it.split(":")[1].split("|").map { str -> str.trim() }
        val winning: List<Int> = cardInput[0].split("\\s+".toRegex()).map { n -> n.toInt() }
        val mine: List<Int> = cardInput[1].split("\\s+".toRegex()).map { n -> n.toInt() }
        cards.add(Card(winning, mine, id))
        id++
    }
    setCopies(cards) // count individual copies
    return cards.sumBy { it.copies } // sum them (use sumOf in newer version)
}

fun setCopies(cards: MutableList<Card>): Unit {
    cards.forEach {
        val nbToUpdate = if (it.matching > cards.size) cards.size else it.matching // don't overflow the list
        // form next card until index + nb of cards to update
        for (i in (it.id)..(it.id - 1 + nbToUpdate)) {
            cards[i].copies += it.copies // if we have multiple copies of a card, we need to add this amount to next cards
        }
    }
}