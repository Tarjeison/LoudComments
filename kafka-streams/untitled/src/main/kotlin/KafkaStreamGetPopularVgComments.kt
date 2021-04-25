import com.beust.klaxon.Klaxon
import org.apache.kafka.common.serialization.Serdes
import org.apache.kafka.streams.KafkaStreams
import org.apache.kafka.streams.StreamsBuilder
import org.apache.kafka.streams.StreamsConfig
import org.apache.kafka.streams.Topology
import org.apache.kafka.streams.kstream.KStream
import java.util.*

class KafkaStreamGetPopularVgComments {

    private fun getStreamProperties(): Properties {
        return Properties().apply {
            put(StreamsConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092")
            put(StreamsConfig.APPLICATION_ID_CONFIG, "stream-test")
            put(StreamsConfig.DEFAULT_KEY_SERDE_CLASS_CONFIG, Serdes.String().javaClass.name)
            put(StreamsConfig.DEFAULT_VALUE_SERDE_CLASS_CONFIG, Serdes.String().javaClass.name)
        }
    }

    private fun getStreamTopology(): Topology {
        val builder = StreamsBuilder()

        // Get a stream of vg comments
        val stream: KStream<String, String> = builder.stream("vg_comments")

        val streamMappedNonNullValues = stream
            //parse json string to data class ("POJO")
            .mapValues { key, value ->
                val vgMessage = try {
                    Klaxon().parse<VgMessage>(
                        value
                    )
                } catch (e: Exception) {
                    e.printStackTrace()
                    null
                }
                vgMessage
            }
            //filterNotNull
            .filter { key, value -> value != null }



        streamMappedNonNullValues
                // getUnpopularComments
            .filter { key, value ->
                try {
                    value!!.downvotesCount.toLong() < value.upvotesCount.toLong()
                } catch (e: Exception) {
                    false
                }
            }.mapValues { value -> value!!.toString() }.to("vg_comments-popular")



        return builder.build()
    }

    fun getStream(): KafkaStreams {
        return KafkaStreams(getStreamTopology(), getStreamProperties())
    }
}

fun main() {
    val stream = KafkaStreamGetPopularVgComments().getStream()
    stream.cleanUp()
    stream.start()

}