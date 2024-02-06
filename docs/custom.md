# Customization Guide

## Creating custom models

Model must use a composition or subclass `redlite.NamedModel`.

Implementation should provide:

1. Model name - a string uniquely identifying this model.

2. A function or method that takes conversation as its input and produces the
   output string.

   Conversation is a list of messages. Each message is a `dict` with just two keys:

   - `role` - can be `"system"`, `"user"` or `"assistant"`.
   - `content` - the message content

    Here is a sample of such an input:

    ```python

    conversation = [
        {'role': 'system', 'content': 'You are a helpful assistant'},
        {'role': 'user', 'content': 'Explain, please, how to bake an egg?'},
        {'role': 'assistant', 'content': 'Take 1 pound of eggs, and add some water...'},
        {'role': 'user', 'content': 'And now, give me a recepie of a cabbage pie!'},
    ]
    ```

### Writing your model code

There are two common ways to write your model: compose, or subclass.

Lets write a model that takes the last message of a conversation and parrots it back.

#### Composing model from a function

Here is the meat of our model:

```python
def parrot(conversation):
    last_message_content = conversation[-1]['content']
    return last_message_content
```

Now we create a model instance like this:

```python
from redlite import NamedModel

def parrot(conversation):
    last_message_content = conversation[-1]['content']
    return last_message_content

model = NamedModel("parrot-model", parrot)
```

We gave it a name of `"parrot-model"`.

#### Subclassing NamedModel

Sometimes prediction logic needs extra state, and can not be easily cast as a function composition.

In such a case we do subclassing:

```python
from redlite import NamedModel


class ParrotModel(NamedModel):

    def __init__(self):
        super().__init__("parrot-model", self.__engine)

    def __engine(self, conversation):
        last_message_content = conversation[-1]['content']
        return last_message_content


model = ParrotModel()
```

IMPORTANT: remember that model name uniquely identifies model instance. Therefore, parametrized models
will construct name from the parameters. For example, lets add truncation parameter to our `ParrotModel`:

```python
from redlite import NamedModel


class TruncatingParrotModel(NamedModel):

    def __init__(self, truncate_to=20):
        self.truncate_to = truncate_to
        super().__init__(f"parrot-model-truncate-{truncate_to}", self.__engine)

    def __engine(self, conversation):
        last_message_content = conversation[-1]['content']
        return last_message_content[:self._truncate_to]


model1 = TruncatingParrotModel(truncate_to=10)
model2 = TruncatingParrotModel(truncate_to=30)
```

This new model will return the last message in the input conversation and also will truncate it to
the specified length.

Note in the code above:

1. Model takes parameter `truncate_to` that tells the model how large the output string can be.
2. When computing the output string this parameter is used to truncate it.
3. Truncation value made part of the model name. This ensures that if two models have the same name, they
   behave identically. In the sample above, `model1` and `model2` will have different names.

## Creating custom metrics

Custom metric must use a composition or subclass `redlite.NamedMetric`.

Implementation should provide:

1. Metric name - a string uniquely identifying this metric.

2. A function or method that takes `expected` and `actual` strings and outputs score.

3. Score is a `float` value in the range `0.0` -- `1.0`. Larger score mens better performance.

### Writing your metric code

Just like with the models, there are two common ways to implement metric: compose from a
function, or subclass `NamedMetric`.

Lets write a metric that outputs `1.0` if `expected` and `actual` strings have the same length, and
outputs `0.0` otherwise.

#### Composing metric from a function

Here is the logic of our metric:

```python
def same_length(expected, actual):
    if len(expected) == len(actual):
        return 1.0
    return 0.0
```

Now we create metric instance like this:

```python
from redlite import NamedMetric

metric = NamedMetric("same-length-metric", same_length)
```

We gave it a name of `"same-length-metric"`.

#### Subclassing NamedMetric

In more complex cases one may need to have state attached to metric. Then subclassing is the right way to go:

```python
from redlite import NamedMetric


class SameLengthMetric(NamedModel):

    def __init__(self):
        super().__init__("same-length-metric", self.__engine)

    def __engine(self, expected, actual):
        if len(expected) == len(actual):
            return 1.0
        return 0.0


model = SameLengthMetric()
```

IMPORTANT: be careful with naming! Remember that metric name uniquely identifies its behavior. For this reason, parametrized metrics
will construct name from the state. For example, lets add tolerance parameter to our `SameLengthMetric`:

```python
from redlite import NamedMetric


class SameLengthWithToleranceMetric(NamedMetric):

    def __init__(self, tolerance=0):
        self.tolerance = tolerance
        super().__init__(f"same-length-tolerance-{tolerance}-metric", self.__engine)

    def __engine(self, expeced, actual):
        if abs(len(expected) - len(actual)) <= self.tolerance:
            return 1.0
        return 0.0


metric1 = SameLengthWithToleranceMetric(tolerance=1)
metric2 = SameLengthWithToleranceMetric(tolerance=2)
```

This new metric tolerates some deviation from the expected length. How big is the tolerance is given by the `tolerance` parameter.

Note in the code above:

1. Metric takes parameter `tolerance` that tells the metric what is the biggest deviation between expected and actual string
   lengths it will tolerate. Default value is 0, making this metric equivalent to the `SameLengthMetric`.
2. When computing the output, `tolerance` is taken into account.
3. Tolerance value is made part of the metric name. This ensures that if two metrics have the same name, they
   behave identically. In the sample above, `metric1` and `metric2` will have different names.
